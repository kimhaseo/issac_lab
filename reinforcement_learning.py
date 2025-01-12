import gym
import numpy as np
from stable_baselines3 import PPO


# 두 관절 로봇 환경 클래스 정의
class TwoJointRobotEnv(gym.Env):
    def __init__(self):
        super(TwoJointRobotEnv, self).__init__()

        # 환경 초기화 (상태 공간과 액션 공간 정의 등)
        self.action_space = gym.spaces.Box(low=-1, high=1, shape=(2,), dtype=np.float32)  # 두 개의 관절에 대한 액션 공간
        self.observation_space = gym.spaces.Box(low=-np.inf, high=np.inf, shape=(4,),
                                                dtype=np.float32)  # 예시로 4개의 상태 값 (두 관절 위치와 속도)

    def reset(self):
        # 환경을 초기화하고 초기 상태를 반환
        self.state = np.zeros(4)  # 초기 상태 설정 (예시)
        return self.state

    def step(self, action):
        # 주어진 액션을 적용하여 새로운 상태 계산
        # 예시로 관절 위치와 속도를 업데이트
        self.state += action  # 간단한 업데이트 (실제 로봇에 맞게 로직 수정 필요)

        # 목표 위치에 가까워졌다면 보상 계산
        distance_to_goal = np.linalg.norm(self.state[:2])  # 예시로 목표 위치는 원점으로 설정
        reward = -distance_to_goal  # 목표에 가까워질수록 보상 증가

        # 종료 조건 (예시로 특정 에피소드 수 이후 종료)
        done = False

        return self.state, reward, done, {}

    def render(self):
        # 환경의 상태를 시각화 (여기서는 간단한 출력)
        print(f"Current state: {self.state}")


# 환경 객체 생성
env = TwoJointRobotEnv()

# 모델 학습
model = PPO("MlpPolicy", env, verbose=1)
model.learn(total_timesteps=100000)

# 학습된 모델 저장
model.save("two_joint_robot_model")
