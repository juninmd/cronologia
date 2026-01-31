import json

def generate_readme():
    with open('projects.json', 'r', encoding='utf-8') as f:
        projects = json.load(f)

    markdown_content = "# cronologia\n\n"

    for project in projects:
        markdown_content += f"## {project['date']} - [{project['name']}]({project['url']})\n"
        markdown_content += f"**Language:** {project['language']} | **Rank:** {project['rank']}\n\n"
        markdown_content += f"> {project['story']}\n\n\n"
        markdown_content += "---\n\n"

    with open('README.md', 'w', encoding='utf-8') as f:
        f.write(markdown_content)

if __name__ == "__main__":
    generate_readme()
