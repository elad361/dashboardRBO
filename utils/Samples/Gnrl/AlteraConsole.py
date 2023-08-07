import subprocess


class altera_system_console:
    def __init__(self):
        sc_path = r'C:\altera\15.0\quartus\sopc_builder\bin\system-console.exe --cli --disable_readline'
        self.console = subprocess.Popen(sc_path, stdin=subprocess.PIPE, stdout=subprocess.PIPE)

    def read_output(self):
        rtn = ""
        loop = True
        i = 0
        match = '%'
        tt =  '-'
        k=0
        while loop:
            out = self.console.stdout.read1(1)
            if bytes(tt, 'utf-8') == out:
                k=k+1
            else:
                k=0

            if bytes(match, 'utf-8') == out:
                i = i + 1
                if i == len(match):
                    loop = False
            else:
                rtn = rtn + out.decode('utf-8')
        return rtn

    def cmd(self, cmd_string):
        self.console.stdin.write(bytes(cmd_string + '\n', 'utf-8'))
        self.console.stdin.flush()


c = altera_system_console()
print(c.read_output())
c.cmd('set ch [lindex [get_service_paths master] 2]')
print(c.read_output())
c.cmd('open_service master $ch')
print(c.read_output())
c.cmd('master_read_memory $ch 0x2000 200')
print(c.read_output())
print(c.read_output())