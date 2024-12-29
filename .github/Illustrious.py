import sys
from pathlib import Path
import _util


def main(args):
  _util.download_model(889818)

  _util.replace_defaults({
    'DEFAULT_VAE_NAME': None,
    'DEFAULT_POS_PREPROMPT': " ",
    'DEFAULT_NEG_PREPROMPT': "",
    'DEFAULT_POSITIVE_PROMPT': "",
    'DEFAULT_NEGATIVE_PROMPT': "",
    'DEFAULT_CFG': 5.5,
    'DEFAULT_CLIP_SKIP': 2,
    'DEFAULT_WIDTH': 1920,
    'DEFAULT_HEIGHT': 1080,
    'DEFAULT_SCHEDULER': "Euler a",
    'DEFAULT_STEPS': 28
  })


if __name__ == '__main__':
  main(sys.argv[1:])
