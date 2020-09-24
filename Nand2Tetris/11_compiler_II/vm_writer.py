class VMWriter:

    KIND_TO_SEGMENT_MAP = {'ARG': 'argument', 'VAR': 'local', 'STATIC': 'static', 'FIELD': 'this', 'CONST': 'constant',
                           'TEMP': 'temp', 'POINTER': 'pointer', 'THAT': 'that'}

    def __init__(self, output_file_path):
        self.output_file = open(output_file_path, 'w')
        self.branching_indexes = {'if': 0, 'while': 0}

    def zero_branching_indexes(self):
        for key in self.branching_indexes:
            self.branching_indexes[key] = 0

    def get_next_label_index(self, statement):
        next_idx = self.branching_indexes[statement]
        self.branching_indexes[statement] += 1
        return next_idx

    def write_push(self, kind, index):
        self.output_file.write('push {0} {1}\n'.format(VMWriter.KIND_TO_SEGMENT_MAP[kind], index))

    def write_pop(self, kind, index):
        self.output_file.write('pop {0} {1}\n'.format(VMWriter.KIND_TO_SEGMENT_MAP[kind], index))

    def write_arithmetic(self, command):
        self.output_file.write('{0}\n'.format(command))

    def write_label(self, label):
        self.output_file.write('label {0}\n'.format(label))

    def write_goto(self, label):
        self.output_file.write('goto {0}\n'.format(label))

    def write_if(self, label):
        self.output_file.write('if-goto {0}\n'.format(label))

    def write_call(self, name, n_args):
        self.output_file.write('call {0} {1}\n'.format(name, n_args))

    def write_function(self, name, n_locals):
        self.output_file.write('function {0} {1}\n'.format(name, n_locals))

    def write_return(self):
        self.output_file.write('return\n')

    def close(self):
        self.output_file.close()
