import yaml
import os
import sys

def read_toc_from_yaml(file_path):
    with open(file_path, 'r') as f:
        data = yaml.safe_load(f)
    toc = data.get('project', {}).get('toc', [])
    return toc

def flatten_toc(toc):
    flat = []
    for item in toc:
        if 'file' in item:
            flat.append(item['file'])
        if 'children' in item:
            flat.extend(flatten_toc(item['children']))
    return flat

def calculate_jb1_slugs(toc_flat):
    return [path.replace('.md', '.html').replace('.ipynb', '.html') for path in toc_flat]

def calculate_jb2_slugs(toc_flat):
    jb2_slugs = [path.replace('.md', '').replace('.ipynb', '').replace('_', '-').lower().replace('chapters/intro', '') for path in toc_flat]
    # chapters/intro.html is a special case that becomes ''
    return jb2_slugs

def create_redirects(jb1_slugs, jb2_slugs, base_url="https://inferentialthinking.com/", output_root="_build/redirects"):
    assert(len(jb1_slugs) == len(jb2_slugs))
    for i in range(len(jb1_slugs)):
        jb1_slug = jb1_slugs[i]
        jb2_slug = jb2_slugs[i]
        # skip markdown files
        # if jb2_slug.endswith('.md'):
        #     continue 
        # create the output directory if it doesn't exist, using a separate redirects dir
        dir = os.path.dirname(jb1_slug)
        output_dir = os.path.join(output_root, dir)
        os.makedirs(output_dir, exist_ok=True)
        # create the full jb2 url
        jb2_url = base_url + jb2_slug + "/index.html"
        # html content
        # simple HTML redirect with a visible link as a fallback
        html_content = f"""<!DOCTYPE html>
            <html>
            <head>
                <meta http-equiv="refresh" content="0; url={jb2_url}">
                <meta charset="utf-8">
                <title>Redirecting...</title>
            </head>
            <body>
                <p>Redirecting to <a href=\"{jb2_url}\">{jb2_url}</a></p>
            </body>
            </html>
            """
        output_file = os.path.join(output_root, jb1_slug)
        with open(output_file, 'w') as f:
            f.write(html_content)


if __name__ == "__main__":
    toc = read_toc_from_yaml('myst.yml')
    toc_flat = flatten_toc(toc)
    jb1_slugs = calculate_jb1_slugs(toc_flat)
    jb2_slugs = calculate_jb2_slugs(toc_flat)
    
    # Handle command line args
    base_url = "https://inferentialthinking.com/"
    output_root = "_build/redirects"
    
    if len(sys.argv) > 1:
        base_url = sys.argv[1]
    if len(sys.argv) > 2:
        output_root = sys.argv[2]
        
    create_redirects(jb1_slugs, jb2_slugs, base_url, output_root)