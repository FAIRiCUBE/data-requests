# issues-yaml-generator

A tool that downloads github issues from the `data-requests` repository nad generate yaml files from the response markdown.

Replace the `GH_TOKEN` in the code with your own github token (`Personal access tokens (classic)`)

```python
GH_TOKEN = "<github-token>"

```
### installation and Quick start


```bash
# installing requirements
pip install -r requirements.txt

# generate the code and save yaml files in the 'yaml' folder

python3 yaml-generator.py


```