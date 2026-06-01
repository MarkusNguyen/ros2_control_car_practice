import mujoco
import mujoco.viewer
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
xml_path = os.path.join(script_dir, 'car.xml')

model = mujoco.MjModel.from_xml_path(xml_path)
data = mujoco.MjData(model)

with mujoco.viewer.launch(model, data) as viewer:
    while viewer.is_running():
        # Step your physics simulation here
        mujoco.mj_step(model, data)
        viewer.sync()