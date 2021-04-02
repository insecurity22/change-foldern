import os
import sys
import re

# 17-2 -> summary0902

path = "C:\\Users\\CT-Kang\\Desktop\\example\\"
oName = "2"
cName = "summary09"
oMiddleText = "-"
cMiddleText = ""
oExtension = ".png"
cExtension = ".png"

# --- 인자값
# 1. 이름을 변경하고 싶은 폴더 경로
# 2. 원본 문자         ex) 17
# 3. 변경할 문자       ex) summary09
# 4. 원본 중간 문자
# 5. 변경할 중간 문자
# 6. 원본 확장자
# 7. 변경할 확장자
# --> 원본과 변경할 확장자가 같을 경우, 같게 입력

def changeName(path, cName):

    count = 0
    for filename in os.listdir(path):
        # 확장자가 다르면 변경할 파일에서 제외
        if re.findall("\.[a-zA-Z0-9]*", filename)[0] != oExtension:
            continue

        try:
            print("\n-------------------------")
            print("[변경 전]")
            print("폴더 이름:", filename)

            print("\n[변경 후]")
            
            # 중간에 구분 문자가 있을 때. ex) 17-2
            if oMiddleText != "":
                # 10 이하는 앞에 0 붙이기
                name = filename.split(".")[0].split(oMiddleText) # ['17', '9']
                if int(name[1]) < 10:
                    index = "0" + name[1]
                else:
                    index = name[1]
                print("폴더 이름:", cName + cMiddleText + index + cExtension)
                print("-------------------------")

            # 변경 확인
            if count == 0:
                print("\n변경 후 폴더 이름을 확인해주세요. 변경하시겠습니까? (Y|N|A|E)")
                # Y : 변경
                # N : 변경하지 않음
                # A : 전체 변경
                # E : 프로그램 종료

                answer = input()
                if answer == "Y" or answer == "N":
                    os.rename(path + filename, path + cName + cMiddleText + index + cExtension)
                    continue
                elif answer == "A": count = 1
                elif answer == "E": sys.exit()
                    
            # 변경
            if count == 1: # Y
                print("\n전체 변경되었습니다.\n")
                os.rename(path+filename, path+cName+cMiddleText+index+cExtension)

        except Exception as e:
            print("--> 변경할 수 없습니다.\n")


if __name__ == "__main__":
    print("\n------------ 입력 값 확인 ----------------")
    print("폴더 경로:", path)
    print("-----------------------------------------\n")

    changeName(path, cName)