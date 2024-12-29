import sys
from pathlib import Path
import _util


def main(args):
  _util.download_model(1053830)

  _util.replace_defaults({
    'DEFAULT_VAE_NAME': None,
    'DEFAULT_POS_PREPROMPT': "masterpiece, best quality, ",
    'DEFAULT_NEG_PREPROMPT': "(lowres:1.2), (worst quality:1.4), (low quality:1.4), (bad anatomy:1.4), bad hands, multiple views, comic, jpeg artifacts, patreon logo, patreon username, web address, signature, watermark, text, logo, artist name, censored",
    'DEFAULT_POSITIVE_PROMPT': "",
    'DEFAULT_NEGATIVE_PROMPT': "",
    'DEFAULT_CFG': 6,
    'DEFAULT_CLIP_SKIP': 2,
    'DEFAULT_WIDTH': 1920,
    'DEFAULT_HEIGHT': 1080,
    'DEFAULT_SCHEDULER': "Euler A",
    'DEFAULT_STEPS': 30
  })


if __name__ == '__main__':
  main(sys.argv[1:])