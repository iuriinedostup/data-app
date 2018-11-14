import argparse
from tasks.load import LoadTaskFactory
from tasks.transform import TransformTaskFactory


parser = argparse.ArgumentParser(description='Patterns App')

task_map = {
    'load': LoadTaskFactory,
    'transform': TransformTaskFactory
}


if __name__ == '__main__':

    sub_parsers = parser.add_subparsers(
        description="Sub parser"
    )

    for name, f in task_map.iteritems():
        subparser = sub_parsers.add_parser(name, help='{}: sub parser'.format(name))
        factory = f.create(subparser)

    args = parser.parse_args()
    args.func(args)
