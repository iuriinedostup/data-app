import argparse


class App(object):

    tasks = {
        'load': LoadData,
        'transform': TransformData
    }

    def __init__(self, parser=None):
        self.parser = parser

    def dispatch(self):
        if not self.parser:
            parser = argparse.ArgumentParser(description='Transformation app')
            parser.add_argument(
                '--task',
                dest='task',
                help='Application name',
                required=True
            )

            self.parser = parser

        self.parser.set_defaults(func=self.run)

    def run(self, args):
        task_class = self.tasks[args.task]
        task = task_class()
        task.execute(args)


class LoadData(object):
    def execute(self, args):
        pass


class TransformData(object):
    def execute(self, args):
        pass


if __name__ == '__main__':
    app = App()
    app.dispatch()
