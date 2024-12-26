import json, subprocess, re, requests
from os import environ as env
from pathlib import Path

_session = requests.Session()



def download_model(download_id: int | str):
  files, h = None, {'Content-Type':"text/json", 'Authorization': f"Bearer {env['CIVITAI_API_TOKEN']}"}
  response = _session.get(f"https://civitai.com/api/v1/models/{download_id}", headers=h).json()

  if response.get('error') == f"No model with id {download_id}":
    response = _session.get(f"https://civitai.com/api/v1/model-versions/{download_id}", headers=h).json()
    files = response['files']
  else:
    files = [f['files'] for f in response['modelVersions'] if f.get('index') == 0][0]

  ckpt = get_checkpoint_file(files)

  url = _session.get(ckpt['downloadUrl'],
    params = {'type': ckpt['type']} | {k: v for k, v in ckpt['metadata'].items() if v},
    headers = {'Authorization': f"Bearer {env['CIVITAI_API_TOKEN']}"},
    allow_redirects=False).content

  aria_dl(url, "models", ckpt['name'])



def get_checkpoint_file(files: list) -> dict:
  def _priority(f):
    match [f['metadata']['fp'], f['metadata']['size']]:
      case ['fp16','pruned']: return 1
      case ['fp16', 'full' ]: return 2
      case ['fp32','pruned']: return 3
      case ['fp32', 'full' ]: return 4
    return 5

  models = [f for f in files if f['type'] == 'Model']

  return sorted(models, key=_priority)[0]



def aria_dl(target_uri: str, target_dir: str, target_filename: str) -> int:
  if (Path.cwd() / target_dir / target_filename).is_file():
    return 0
  s = subprocess.run([
    '.github/.bin/aria2c', '-c',
    '--check-certificate=false',
    '--max-connection-per-server=16',
    '--split=16',
    '--max-tries=10',
    '--content-disposition-default-utf8',
    '--http-accept-gzip',
    '--file-allocation=falloc',
    '--console-log-level=error',
    '--show-console-readout=false',
    '--summary-interval=2',
    '--download-result=full',
    '--dir', f"{Path.cwd() / target_dir}",
    '--out', target_filename,
    target_uri
  ])
  if s.returncode == 0:
    return 0
  raise Exception(f'download "{target_uri}" failed')



def replace_defaults(new_defaults: dict):
  path = Path('constants.py')
  content = path.read_text()
  for var, replacement in new_defaults.items():
    pattern = rf'^(\s*{var}\s*=\s*)(.+)$'
    if type(replacement) == str:
      replacement = f'"{replacement}"'
    content, num_subs = re.subn(pattern, rf'\g<1>{replacement}', content, flags=re.MULTILINE)
    if num_subs == 0 : raise RuntimeError(f"'{var}' not found in {path}.")
    elif num_subs > 1: raise RuntimeError(f"'{var}' is present too many times in {path}.")
  path.write_text(content)
