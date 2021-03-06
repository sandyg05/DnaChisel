"""Basic demo of the high-level method optimization_with_report."""
import os
from dnachisel.reports import optimization_with_report

genbank_path = os.path.join("data", "example_sequence.gbk")
report_folder = os.path.join("reports", "optimization_with_report")

success, message, _ = optimization_with_report(target=report_folder,
                                               record=genbank_path)

print(message + " A report was generated in " + report_folder)
