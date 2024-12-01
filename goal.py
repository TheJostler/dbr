from pip._internal.locations import USER_CACHE_DIR as user_cache_dir

datadir = user_cache_dir.replace("/.cache/pip", "/.cache/dbr")

if __name__ == "__main__":
  with open(f"{datadir}/goal", 'r') as g:
    print(g.read())