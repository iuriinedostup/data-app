import argparse
from tasks.load import LoadTaskFactory
from tasks.transform import TransformTaskFactory


parser = argparse.ArgumentParser(description='Patterns App')

parser.add_argument(
    '--task',
    dest='task',
    choices=['load', 'transform']
)


if __name__ == '__main__':

    args = parser.parse_args()

    if args.task == 'load':
        task = LoadTaskFactory.create()
    elif args.task == 'transform':
        task = TransformTaskFactory.create()
    else:
        raise ValueError('Incorrect task name')

    task.execute()
