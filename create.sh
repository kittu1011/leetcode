#!/bin/bash
CACHE=".name_cache.json"
TEMPLATE="templates/notes_template.md"

[ -f "$CACHE" ] || echo '{}' > "$CACHE"

problem_number=$1
if [ -z "$problem_number" ]; then
    echo "Usage: create [problem number]"
    exit 1
fi

if [ ! -f "$TEMPLATE" ]; then
    echo "Template not found at $TEMPLATE"
    exit 1
fi

# Pad number to 4 digits
padded=$(printf "%04d" $problem_number)

# Check cache first (keyed by problem number)
cached=$(jq -r --arg num "$problem_number" '.[$num]' "$CACHE")

if [ "$cached" != "null" ] && [ -n "$cached" ]; then
    title_slug=$(echo "$cached" | jq -r '.titleSlug')
    difficulty=$(echo "$cached" | jq -r '.difficulty')
else
    # Query by frontend ID using current schema (questionList aliased as problemsetQuestionList)
    response=$(curl -s -X POST https://leetcode.com/graphql \
        -H "Content-Type: application/json" \
        -H "Cookie: LEETCODE_SESSION=$LEETCODE_SESSION" \
        -d "$(jq -n --arg num "$problem_number" '{
            query: "query problemsetQuestionList($categorySlug: String, $limit: Int, $skip: Int, $filters: QuestionListFilterInput) { problemsetQuestionList: questionList(categorySlug: $categorySlug, limit: $limit, skip: $skip, filters: $filters) { questions: data { questionFrontendId titleSlug difficulty } } } ",
            variables: { categorySlug: "", skip: 0, limit: 1, filters: { searchKeywords: $num } }
        }')")

    title_slug=$(echo "$response" | jq -r '.data.problemsetQuestionList.questions[0].titleSlug')
    difficulty=$(echo "$response" | jq -r '.data.problemsetQuestionList.questions[0].difficulty')

    if [ "$title_slug" = "null" ] || [ -z "$title_slug" ]; then
        echo "Could not find problem $problem_number"
        exit 1
    fi

    # Write to cache as a nested object: { "42": { "titleSlug": "...", "difficulty": "..." } }
    jq --arg num "$problem_number" --arg slug "$title_slug" --arg diff "$difficulty" \
        '.[$num] = { "titleSlug": $slug, "difficulty": $diff }' "$CACHE" > temp.json && mv temp.json "$CACHE"
fi

# Human-readable title from slug, e.g. longest-valid-parentheses -> Longest Valid Parentheses
title=$(echo "$title_slug" | sed 's/-/ /g' | sed -e 's/\b\(.\)/\u\1/g')

echo "Problem: $title_slug ($difficulty)"
echo ""
echo "Available folders:"
ls -d */ | grep -v ".git"
echo ""

# Read folder with tab-autocomplete against existing top-level directories
folders=$(ls -d */ 2>/dev/null | grep -v ".git" | sed 's#/$##')

_complete_folder() {
    local cur=${COMP_WORDS[COMP_CWORD]}
    COMPREPLY=( $(compgen -W "$folders" -- "$cur") )
}
complete -F _complete_folder read

read -e -p "Folder: " folder

folder="${folder%/}"  # strip trailing slash if they added one

if [ ! -d "$folder" ]; then
    echo "Folder '$folder' does not exist"
    exit 1
fi

problem_dir="$folder/${padded}-${title_slug}"

if [ -d "$problem_dir" ]; then
    echo "Problem folder '$problem_dir' already exists"
    exit 1
fi

mkdir -p "$problem_dir"

# solution.py stub
cat > "$problem_dir/solution.py" << EOF
# LeetCode $problem_number: $title
class Solution:
    pass
EOF

# notes.md from template with frontmatter substitutions
sed \
    -e "s/{{TITLE}}/$title/" \
    -e "s/{{NUMBER}}/$problem_number/" \
    -e "s/{{DIFFICULTY}}/$difficulty/" \
    "$TEMPLATE" > "$problem_dir/notes.md"

echo ""
echo "Created:"
echo "  $problem_dir/solution.py"
echo "  $problem_dir/notes.md"