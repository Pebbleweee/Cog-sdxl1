import sys
from pathlib import Path
import _util


def main(args):
  _util.download_model(1166878)

  _util.replace_defaults({
    'DEFAULT_VAE_NAME': None,
    'DEFAULT_POS_PREPROMPT': "masterpiece, best quality, newest, absurdres, highres, ",
    'DEFAULT_NEG_PREPROMPT': "worst quality, old, early, low quality, lowres, signature, username, logo, bad hands, mutated hands,",
    'DEFAULT_POSITIVE_PROMPT': "",
    'DEFAULT_NEGATIVE_PROMPT': "",
    'DEFAULT_CFG': 5.8,
    'DEFAULT_CLIP_SKIP': 2,
    'DEFAULT_WIDTH': 1920,
    'DEFAULT_HEIGHT': 1080,
    'DEFAULT_SCHEDULER': "DPM++ 2M",
    'DEFAULT_STEPS': 28
  })


if __name__ == '__main__':
  main(sys.argv[1:])