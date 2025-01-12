from omni.isaac.kit import SimulationApp
from omni.isaac.core import World
from omni.isaac.core.objects import Articulation

# Isaac Sim 초기화
simulation_app = SimulationApp({"headless": False})

# 시뮬레이션 환경 생성
world = World(stage_units_in_meters=1.0)
world.scene.add_default_ground_plane()

# 로봇 로드
robot = Articulation("/World/two_joint_robot")
robot.initialize()

# 시뮬레이션 실행 루프
world.reset()
for _ in range(100):
    # 관절 제어
    robot.set_joint_positions([0.5, -0.5])  # 각도 설정 (라디안)
    world.step(render=True)

# Isaac Sim 종료
simulation_app.close()
