import random
from datetime import datetime, timedelta
from faker import Faker
import pathlib

COUNT_LINES = 10_000

PROJECT_PATH = pathlib.Path(__file__).parent
fake = Faker()
devices = ["MacBook", "Ubuntu-18.04", "AstraLinux", "Windows 10", "Android", "iPhone"]


class GeneratorLogs:
    """Generate data logs"""

    log_format = "{timestamp} {device}: {facility}-{level}-{number}: {message}\n"
    output_file = (PROJECT_PATH / "output.log").resolve()

    def run(self) -> None:
        with open(self.output_file, "w") as log:
            now = datetime.now()
            delta = timedelta(hours=1)
            for i in range(COUNT_LINES):
                now += delta
                log.write(self.log_format.format(
                    timestamp=now.strftime("%Y-%m-%d %H:%M:%S"),
                    device=random.choice(devices),
                    facility=random.randrange(24),
                    level=random.randrange(8),
                    number=i,
                    message=fake.sentence(nb_words=10)
                ))


if __name__ == "__main__":
    generator = GeneratorLogs()
    generator.run()
