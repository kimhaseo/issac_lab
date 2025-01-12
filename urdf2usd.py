from omni.isaac.urdf.importer import URDFImporter

# URDF 파일 경로
urdf_file_path = "/home/username/urdf/two_joint_robot.urdf"

# 변환 결과를 저장할 USD 파일 경로
usd_file_path = "/home/username/urdf_output/two_joint_robot.usd"

# URDF를 USD로 변환
importer = URDFImporter()
importer.import_urdf(urdf_path=urdf_file_path, output_path=usd_file_path)

print("URDF 변환 완료:", usd_file_path)
