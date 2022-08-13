from project.hardware.heavy_hardware import HeavyHardware
from project.hardware.power_hardware import PowerHardware
from project.software.express_software import ExpressSoftware
from project.software.light_software import LightSoftware
from project.software.software import Software


class System:
    _hardware = []
    _software = []

    def __init__(self):
        pass

    @staticmethod
    def register_power_hardware(name: str, capacity: int, memory: int):
        power_hardware = PowerHardware(name, capacity, memory)
        System._hardware.append(power_hardware)

    @staticmethod
    def register_heavy_hardware(name: str, capacity: int, memory: int):
        heavy_hardware = HeavyHardware(name, capacity, memory)
        System._hardware.append(heavy_hardware)

    @staticmethod
    def register_express_software(hardware_name: str, name: str, capacity_consumption: int, memory_consumption: int):
        hardware = [h for h in System._hardware if h.name == hardware_name]
        if not hardware:
            return 'Hardware does not exist'
        hardware = hardware[0]
        express_software = ExpressSoftware(name, capacity_consumption, memory_consumption)
        try:
            hardware.install(express_software)
            System._software.append(express_software)
        except Exception as ex:
            return str(ex)

    @staticmethod
    def register_light_software(hardware_name: str, name: str, capacity_consumption: int, memory_consumption: int):
        hardware = [h for h in System._hardware if h.name == hardware_name]
        if not hardware:
            return 'Hardware does not exist'
        hardware = hardware[0]
        light_software = LightSoftware(name, capacity_consumption, memory_consumption)
        try:
            hardware.install(light_software)
            System._software.append(light_software)
        except Exception as ex:
            return str(ex)

    @staticmethod
    def release_software_component(hardware_name: str, software_name: str):
        hardware = [h for h in System._hardware if h.name == hardware_name]
        software = [s for s in System._software if s.name == software_name]
        if not hardware or not software:
            return 'Some of the components do not exist'
        hardware = hardware[0]
        software = software[0]
        hardware.uninstall(software)
        System._software.remove(software)

    @staticmethod
    def analyze():
        s_memory = sum([s.memory_consumption for s in System._software])
        h_memory = sum([h.memory for h in System._hardware])
        total_memory = f'{s_memory}' + ' / ' + f'{h_memory}'
        total_capacity = f'{sum([s.capacity_consumption for s in System._software])}' + ' / ' +\
                         f'{sum([h.capacity for h in System._hardware])}'

        return f'System Analysis\nHardware Components: {len(System._hardware)}\n' \
               f'Software Components: {len(System._software)}\n' \
               f'Total Operational Memory: {total_memory}\n' \
               f'Total Capacity Taken: {total_capacity}'

    @staticmethod
    def system_split():
        result = ''
        for hardware in System._hardware:
            result += f'Hardware Component - {hardware.name}\n'

            result += f"Express Software Components:" \
                      f" {len([s for s in hardware.software_components if s.__class__.__name__ == 'ExpressSoftware'])}\n"
            result += f"Light Software Components: " \
                      f"{len([s for s in hardware.software_components if s.__class__.__name__ == 'LightSoftware'])}\n"
            result += f"Memory Usage: {sum([s.memory_consumption for s in hardware.software_components])}" + ' / ' +\
                      f"{hardware.memory}\n"
            result += f'Capacity Usage: {sum([s.capacity_consumption for s in hardware.software_components])}' + ' / ' +\
                      f'{hardware.capacity}\n'
            result += f'Type: {hardware.hardware_type}\n'
            s_names = []
            for s in hardware.software_components:
                if not s.name:
                    s_names.append('None')
                s_names.append(s.name)
            result += f"Software Components: {', '.join(s_names)}\n"

        return result.strip()


