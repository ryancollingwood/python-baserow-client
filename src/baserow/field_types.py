import dataclasses
import enum
import typing as t

from databind.core.settings import Union

from .types import TableField


class NumberType(enum.Enum):
  INTEGER = enum.auto()
  DECIMAL = enum.auto()


class DateFormat(enum.Enum):
  EU = enum.auto()
  US = enum.auto()
  ISO = enum.auto()


# Getting an error that `field('date') is not part of FormulaType`
class FormulaType(enum.Enum):
  INVALID = enum.auto()
  TEXT = enum.auto()
  CHAR = enum.auto()
  LINK = enum.auto()
  DATE = enum.auto()
  DATE_INTERVAL = enum.auto()
  BOOLEAN = enum.auto()
  NUMBER = enum.auto()
  SINGLE_SELECT = enum.auto()


@dataclasses.dataclass
class SelectOption:
  id: int
  value: str
  color: str


@Union.register(TableField, 'text')
@dataclasses.dataclass
class TextTableField(TableField):
  text_default: str


@Union.register(TableField, 'long_text')
@dataclasses.dataclass
class LongTextTableField(TableField): pass


@Union.register(TableField, 'number')
@dataclasses.dataclass
class NumberTableField(TableField):
  number_decimal_places: int
  number_negative: bool


@Union.register(TableField, 'single_select')
@dataclasses.dataclass
class SingleSelectTableField(TableField):
  select_options: t.List[SelectOption]


@Union.register(TableField, 'multiple_select')
@dataclasses.dataclass
class MultipleSelectTableField(TableField):
  select_options: t.List[SelectOption]


@Union.register(TableField, 'url')
@dataclasses.dataclass
class UrlTableField(TableField):
  pass


@Union.register(TableField, 'link_row')
@dataclasses.dataclass
class LinkRowTableField(TableField):
  link_row_table: int
  link_row_related_field: int


@Union.register(TableField, 'boolean')
@dataclasses.dataclass
class BooleanTableField(TableField): 
  pass


@Union.register(TableField, 'file')
@dataclasses.dataclass
class FileTableField(TableField): 
  pass


@Union.register(TableField, 'date')
@dataclasses.dataclass
class DateTableField(TableField):
  date_format: DateFormat
  date_include_time: bool
  date_time_format: str
  date_show_tzinfo: bool
  date_force_timezone: t.Optional[str]
  date_force_timezone_offset: t.Optional[int]


@Union.register(TableField, 'rating')
@dataclasses.dataclass
class RatingTableField(TableField):
  max_value: int
  color: str
  style: str


@Union.register(TableField, 'formula')
@dataclasses.dataclass
class FormulaTableField(TableField):
  date_time_format: t.Optional[str]
  date_show_tzinfo: t.Optional[bool]
  date_force_timezone: t.Optional[str]
  array_formula_type: t.Optional[str]
  date_format: t.Optional[DateFormat]
  date_include_time: t.Optional[bool]
  number_decimal_places: t.Optional[int]
  formula: str
  formula_type: str
  nullable: bool
  error: t.Optional[str]
