import asyncio
from viam.module.module import Module
try:
    from models.sample_sensor import SampleSensor
except ModuleNotFoundError:
    # when running as local module with run.sh
    from .models.sample_sensor import SampleSensor


if __name__ == '__main__':
    asyncio.run(Module.run_from_registry())
