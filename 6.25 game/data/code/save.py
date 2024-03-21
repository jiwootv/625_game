# save code

class Save:
    def __init__(self):
        self._file_w = (
"""Name
1
"""
        )
        self.file0 = open(r"data\save\file0", "r", encoding="UTF8")
        self.file1 = open(r"data\save\file1", "r", encoding="UTF8")
        self.file2 = open(r"data\save\file2", "r", encoding="UTF8")
        self.file0_r = self.file0.readlines()
        self.file1_r = self.file1.readlines()
        self.file2_r = self.file2.readlines()
        if not self.file0_r:
            self.file0_r = ["None"]

        if not self.file1:
            self.file1_r = ["None"]

        if not self.file2:
            self.file2_r = ["None"]
        print(self.file0_r)
        self.file0.close()
        self.file1.close()
        self.file2.close()

        self.file0 = open(r"data\save\file0", "w", encoding="UTF8")
        self.file1 = open(r"data\save\file1", "w", encoding="UTF8")
        self.file2 = open(r"data\save\file2", "w", encoding="UTF8")
        self.ROOMLIST = ["없음", "감옥", "감옥 복도", "감옥 복도"]
        # load file
        self.Pname = ""
        self.P_room = 0
        self.P_gun = 0

    def __roomlist(self):
        return self.ROOMLIST

    def edit(self, type, r, filenum):
        if filenum == 0:
            if type == "name":
                if len(self.file0_r) == 0: self.file0_r.append(r)
                else: self.file0_r[0] = r
        if filenum == 1:
            if type == "name":
                if len(self.file1_r) == 0: self.file1_r.append(r)
                else: self.file1_r[0] = r
        if filenum == 2:
            if type == "name":
                if len(self.file2_r) == 0: self.file2_r.append(r)
                else: self.file2_r[0] = r


    def write(self):
        print("File")
        for i in self.file0_r:
            self.file0.write(i)
        for i in self.file1_r:
            self.file1.write(i)
        for i in self.file2_r:
            self.file2.write(i)
        self.file0.close()
        self.file1.close()
        self.file2.close()

    def is_none(self, file_number):
        print(eval('self.file{}_r[0]=="None"'.format(file_number, file_number)))
        print(bool(eval('self.file{}_r[0] == "None"'.format(file_number, file_number))))
        return bool(eval('self.file{}_r[0] == "None"'.format(file_number, file_number)))

    def load(self, type, filenum):
        return eval(f"self.file{filenum}_r[{type}]")


class Save_Ini:
    def __init__(self):
        from configparser import ConfigParser

        self.config = ConfigParser()

        ret = self.config.read(r'data\save\t.ini')

        found = False
        if not ret:
            print("INI 파일이 존재하지 않음")
        else:
            found = True
            print("INI 파일 존재")

        # INI 파일이 존재하지 않으면 INI 파일을 생성합니다.
        if not found:
            self.config.add_section('Setting')
            self.config.set('Setting', '_SE_Volume', '1.00')
            self.config.set('Setting', '_MUS_Volume', '1.00')
            self.config.set('Setting', 'Difficult', 'True')

            self.config.add_section("Achievement")
            self.config.set("Achievement", "_CLEAR_NUMBER", "0")
            self.config.set("Achievement", "_M_ISTEREGG", "0")

            with open(r'data\save\t.ini', 'w') as configfile:
                configfile.write("# 누군가 이 1950 : 정지 파일을 보고 있네요\n# 같은 게임 뜯기 좋아하는 사람으로써 너무 고맙습니다..\n")
                self.config.write(configfile)

            print('INI 파일 생성')

        self._SE_Volume = self.config.get("Setting", "_SE_Volume")
        self._MUS_Volume = self.config.get("Setting", "_MUS_Volume")
        self.Difficult = self.config.get("Setting", "Difficult")
        self.E_M = self.config.get("Achievement", "_m_isteregg")
        print(self.E_M)

    def get_ini(self, t):
        a = eval(f"self.{t}")
        return a

    def edit_ini(self, s, o, r):
        self.config.set(s, o, r)
        with open(r'data\save\t.ini', 'w') as configfile:
            self.config.write(configfile)

# print(Save_Ini().get_ini("_SE_Volume"))

# INI 파일이 존재하면 읽어와서 출력하고 일부 값을 변경해서 다시 저장합니다.
