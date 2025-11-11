from gym.spaces import Discrete, Box
import numpy as np

import sys
from os.path import dirname, abspath

sys.path.append(dirname(dirname(abspath(__file__))))

from envs.DWA.parameter_tuning_envs import RANGE_DICT as dwa_equation
from envs.Eband.parameter_tuning_envs import RANGE_DICT as eband_equation
from envs.Teb.parameter_tuning_envs import RANGE_DICT as teb_equation

class InfoEnv:
    """ The infomation environment contains observation space and action space infomation only
    """
    def __init__(self, config):
        env_config = config["env_config"]
        env_id = env_config["env_id"]

        if env_id.startswith("dwa_param-v0"):

            self.param_init = self.param_list = np.array([
                0.5, 1.57, 6, 20, 0.75, 1, 0.3
            ])

            self.action_space = Box(
                low=np.array([dwa_equation[k][0] for k in env_config["kwargs"]["param_list"]]),
                high=np.array([dwa_equation[k][1] for k in env_config["kwargs"]["param_list"]]),
                dtype=np.float32
            )

            self.observation_space = Box(
                low=0,
                high=env_config["kwargs"]["laser_clip"],
                shape=(721,),
                dtype=np.float32
            )

        elif env_id.startswith("teb_param-v0"):

            self.param_list = ['p', 'total_time', 'time_steps', 'blend']
            self.param_init = np.array([1.4, 2, 20, 0])

            self.action_space = Box(
                low=np.array([dwa_equation[k][0] for k in self.param_list]),
                high=np.array([dwa_equation[k][1] for k in self.param_list]),
                dtype=np.float32
            )
        elif env_id.startswith("eband_param-v0"):

            self.param_list = ['p', 'total_time', 'time_steps', 'blend']
            self.param_init = np.array([1.4, 2, 20, 0])

            self.action_space = Box(
                low=np.array([dwa_equation[k][0] for k in self.param_list]),
                high=np.array([dwa_equation[k][1] for k in self.param_list]),
                dtype=np.float32
            )
        else:
            raise NotImplementedError


        self.config = config
