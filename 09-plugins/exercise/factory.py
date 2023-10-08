from dataclasses import dataclass, field
from decimal import Decimal
from typing import Callable

ProcessorFunc = Callable[[Decimal], None]


@dataclass
class PaymentProcessorFactory:
    processors: dict[str, ProcessorFunc] = field(default_factory=dict)

    def register(self, processor_name: str, processor_func: ProcessorFunc) -> None:
        self.processors[processor_name] = processor_func

    def unregister(self, processor_name: str) -> None:
        self.processors.pop(processor_name)

    def get(self, processor_name: str) -> ProcessorFunc:
        return self.processors[processor_name]

    def list_processors(self) -> list[str]:
        return list(self.processors.keys())


payment_processor_factory = PaymentProcessorFactory()
