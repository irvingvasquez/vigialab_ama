import argparse

#  Argument parser
if __name__ == "__main__":
    ap = argparse.ArgumentParser()

    ap.add_argument("-tp", "--train_path", required=True, help="train folder path")
    args = vars(ap.parse_args())

    print(args['train_path'])

