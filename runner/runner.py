import docker


class Runner:

    def __init__(self, filename) -> None:

        self.client = docker.from_env()
        self.filename = filename
        self.program_name = filename.split('.')[0]

        self.working_dir = '/tmp/shotgun/'
        self.container = None
        self.run_results = None
        self.output = None

        self._compiled = False
        self._parsed_run_results = False

    def run(self):

        if self._compiled is False:
            self._compile()

        if self._parsed_run_results is False:
            self._parse_run_results()

    def _compile(self):

        if self._compiled is True:
            return

        print('Compiling...')

        time_command = 'time {} > {}.log'.format(
            self.program_name, self.program_name
        )

        command = '/bin/bash -c "gcc -o {} {} && {} && rm {}"'.format(
            self.program_name, self.filename, time_command, self.program_name
        )

        self.container = self.client.containers.run(
            image='gcc:4.9',
            command=command,
            volumes={
                self.working_dir: {'bind': self.working_dir, 'mode': 'rw'},
            },
            working_dir=self.working_dir,
            auto_remove=False,
            detach=True,
        )

        print('Compiled...')
        self._compiled = True

    def _parse_run_results(self):

        if self._parsed_run_results is True:
            return

        run_results = dict()

        for line in self.container.logs(stream=True):
            l = line.strip().decode("utf-8")

            print(l)
            if l.startswith('user'):
                run_results['user'] = l.split('	')[1]
            elif l.startswith('real'):
                run_results['real'] = l.split('	')[1]
            elif l.startswith('sys'):
                run_results['sys'] = l.split('	')[1]

        self._parsed_run_results = True
        self.run_results = run_results

        with open('{}.log'.format(self.program_name), 'r') as myfile:
            v = myfile.read().replace('\n', '')
            self.output = v

        self.container.remove()
        self._compiled = False
