import sys
from pathlib import Path
import _util


def main(args):
  _util.download_model(1046043)

  _util.replace_defaults({
    'DEFAULT_VAE_NAME': None,
    'DEFAULT_POS_PREPROMPT': "score_9, score_8_up, score_7_up, classic anime",
    'DEFAULT_NEG_PREPROMPT': "score_6, score_5, score_4, lowres, bad anatomy, bad hands, signature, watermarks, ugly, imperfect eyes, skewed eyes, unnatural face, unnatural body, error, extra limb, missing limbs, bad art, bad painting, bad photo, bad image, ",
    'DEFAULT_POSITIVE_PROMPT': "safe",
    'DEFAULT_NEGATIVE_PROMPT': "",
    'DEFAULT_CFG': 7,
    'DEFAULT_CLIP_SKIP': 2,
    'DEFAULT_WIDTH': 1024,
    'DEFAULT_HEIGHT': 1024,
    'DEFAULT_SCHEDULER': "Euler a",
    'DEFAULT_STEPS': 40
  })


if __name__ == '__main__':
  main(sys.argv[1:])
