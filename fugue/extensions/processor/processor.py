from abc import ABC, abstractmethod

from fugue.dataframe import DataFrame, DataFrames
from fugue.extensions.context import ExtensionContext


class Processor(ExtensionContext, ABC):
    """The interface to process one or multiple incoming dataframes and return one
    DataFrame. For example dropping a column of df should be a type of Processor.
    Processor is task level extension, running on driver, and execution engine aware.

    :Notice:
    Before implementing this class, do you really need to implement this
    interface? Do you know the interfaceless feature of Fugue? Implementing Processor
    is commonly unnecessary. You can choose the interfaceless approach which may
    decouple your code from Fugue.
    """

    @abstractmethod
    def process(self, dfs: DataFrames) -> DataFrame:  # pragma: no cover
        """Process the collection of dataframes on driver side

        :Notice:
        * It runs on driver side
        * The dataframes are not necessarily local, for example a SparkDataFrame
        * It is engine aware, you can put platform dependent code in it (for example
        native pyspark code) but by doing so your code may not be portable. If you
        only use the functions of the general ExecutionEngine, it's still portable.

        :param dfs: dataframe collection to operate on
        :return: result dataframe
        """
        raise NotImplementedError