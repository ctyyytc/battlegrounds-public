"""Create a local review copy from PUBLIC_FILES.json; never publish or upload."""
import argparse,hashlib,json,pathlib,re
ROOT=pathlib.Path(__file__).resolve().parents[1]

def digest(path):return hashlib.sha256(path.read_bytes()).hexdigest()

def main():
 p=argparse.ArgumentParser(description=__doc__);p.add_argument('--output',type=pathlib.Path,required=True);a=p.parse_args();out=a.output.resolve()
 if out.exists() or out==ROOT or out.is_relative_to(ROOT):raise ValueError('Output must be a new directory outside this project')
 manifest=json.loads((ROOT/'PUBLIC_FILES.json').read_text('utf-8-sig'));paths=[]
 for entry in manifest['files']:
  rel=pathlib.PurePosixPath(entry['path']);source=ROOT/rel
  if rel.is_absolute() or '..' in rel.parts or ':' in str(rel) or source.is_symlink() or not source.resolve().is_relative_to(ROOT):raise ValueError('Invalid manifest path')
  if str(rel).startswith(('addons/','.godot/','local_resources/','builds/','.godot_ai')):raise ValueError('Private entry in manifest')
  if digest(source)!=entry['sha256']:raise ValueError('Source changed: '+str(rel))
  paths.append((rel,source))
 out.mkdir(parents=True)
 for rel,source in paths:
  target=out/rel;target.parent.mkdir(parents=True,exist_ok=True);data=source.read_bytes()
  if str(rel)=='project.godot':
   text=data.decode('utf-8-sig');text=re.sub(r'^_mcp_game_helper=.*\r?\n','',text,flags=re.M)
   text=re.sub(r'\[editor_plugins\][\s\S]*?(?=\n\[|\Z)','',text)
   data=text.encode('utf-8')
  target.write_bytes(data)
 manifest['files']=[{'path':str(rel),'sha256':digest(out/rel),'bytes':(out/rel).stat().st_size} for rel,_ in paths]
 manifest['local_plugin_settings_removed']=True
 (out/'PUBLIC_FILES.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n','utf-8')
 print(json.dumps({'created':str(out),'files':len(paths)+1,'local_plugin_settings_removed':True}))
if __name__=='__main__':
 try:main()
 except (OSError,ValueError) as exc:raise SystemExit(str(exc))
