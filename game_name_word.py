import random
import time
from colorama import Fore, Style, init

init(autoreset=True)  # Automatically reset colors after each print statement

skills = [
    {'name': '缠绕', 'power': 10, 'color': Fore.GREEN},
    {'name': '寄生', 'power': 20, 'color': Fore.YELLOW},
    {'name': '蛛网束缚', 'power': 30, 'color': Fore.BLUE},
    {'name': '蓝银囚笼', 'power': 40, 'color': Fore.CYAN},
    {'name': '蓝银霸王枪', 'power': 50, 'color': Fore.MAGENTA},
    {'name': '送去吉大', 'power': 6000, 'color': Fore.WHITE},
    {'name': '武魂真身森罗万象', 'power': 70, 'color': Fore.GREEN},
    {'name': '蓝银邪魔镜之灭', 'power': 80, 'color': Fore.YELLOW},
    {'name': '蓝银天青龙之魂', 'power': 90, 'color': Fore.BLUE},
    {'name': '黄金十三戟', 'power': 100, 'color': Fore.CYAN},
]

def generate_power(name):
    battle_power = sum([ord(c) for c in name])
    attack_power = int(battle_power * 10) + random.randint(30, 50)  # 提高攻击力的随机范围
    defense_power = int(battle_power / 20) + random.randint(10, 20)
    health = int(battle_power / 5) + random.randint(50, 100)  # 降低血量的随机范围

    return attack_power, defense_power, health


def choose_skill(player, under_attack=False):
    available_skills = [skill for skill in skills if skill['power'] <= player['attack_power']]
    
    if under_attack:
        if random.random() <= 0.1:  # 10% 的概率选择无敌金身
            available_skills = [skill for skill in available_skills if skill['name'] == '无敌金身']
        else:
            available_skills = [skill for skill in available_skills if skill['name'] != '无敌金身']
    else:
        if random.random() <= 0.01:  # 1% 的概率选择送去吉大
            available_skills = [skill for skill in available_skills if skill['name'] == '送去吉大']
        else:
            available_skills = [skill for skill in available_skills if skill['name'] != '送去吉大']
    
    # 检查 available_skills 是否为空，如果为空，给出一个默认技能
    if not available_skills:
        available_skills = [{'name': '普通攻击', 'power': 5}]
        
    chosen_skill = random.choice(available_skills)
    return chosen_skill



def attack(attacker, defender):
    attacker_skill = choose_skill(attacker)
    defender_skill = choose_skill(defender, under_attack=True)
    
    if defender_skill['name'] == '无敌金身':
        print(Fore.RED + defender['name'] + "使用无敌金身，免疫本回合伤害。")
    else:
        damage = attacker_skill['power'] * 10
        defender['health'] -= damage
        print(Fore.RED + attacker['name'] + Style.RESET_ALL + "使用" + attacker_skill['color'] + attacker_skill['name'] + Style.RESET_ALL + "攻击了" + Fore.RED + defender['name'] + Style.RESET_ALL + "，造成了" + str(damage) + "点伤害")


def show_status(player1, player2):
    print("--------------------------------")
    print(player1['name'] + "的血量：" + str(player1['health']))
    print(player2['name'] + "的血量：" + str(player2['health']))
    print("--------------------------------")

def start_game():
    player1 = {}
    player2 = {}

    player1['name'] = input("请输入玩家1的名字：")
    player2['name'] = input("请输入玩家2的名字：")

    player1['attack_power'], player1['defense_power'], player1['health'] = generate_power(player1['name'])
    player2['attack_power'], player2['defense_power'], player2['health'] = generate_power(player2['name'])

    print(Fore.RED + player1['name'] +Style.RESET_ALL + "的战斗力：" + Style.RESET_ALL + str(player1['attack_power'] + player1['defense_power'] + player1['health']))
    print(Fore.RED + player2['name'] + Style.RESET_ALL +"的战斗力：" + Style.RESET_ALL + str(player2['attack_power'] + player2['defense_power'] + player2['health']))

    # 添加以下两行代码，显示玩家的初始血量
    print(Fore.RED + player1['name'] +Style.RESET_ALL + "的初始血量：" + Style.RESET_ALL + str(player1['health']))
    print(Fore.RED + player2['name'] + Style.RESET_ALL +"的初始血量：" + Style.RESET_ALL + str(player2['health']))

    while True:
        time.sleep(1)
        attack(player1, player2)
        if player2['health'] <= 0:
            print(Fore.RED +player1['name'] + Style.RESET_ALL + "胜利！")
            break
        time.sleep(1)
        attack(player2, player1)
        if player1['health'] <= 0:
            print(Fore.RED + +player2['name'] + Style.RESET_ALL + "胜利！")
            break
        show_status(player1, player2)

start_game()


