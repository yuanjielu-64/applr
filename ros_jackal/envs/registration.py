from gym.envs.registration import register

register(
    id="eband_param-v0",
    entry_point="envs.Eband.parameter_tuning_envs:AdaptiveDynamicsPlanning_Continues"
)

register(
    id="teb_param-v0",
    entry_point="envs.Teb.parameter_tuning_envs:DWAParamContinuousLaser"
)

register(
    id="dwa_param-v0",
    entry_point="envs.DWA.parameter_tuning_envs:DWAParamContinuousLaser"
)