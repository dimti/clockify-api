from typing import List
from clockify.model.reports_model import SummaryReport, SummaryReportGetParams
from clockify.config import REPORTS_URL
from clockify.wrapper import Wrapper


class ReportsApi(Wrapper):
    def summary(
        self, workspace_id: str, params: SummaryReportGetParams
    ) -> bytes | str | SummaryReport:
        """Return bytes of Summary report if export type one of biary file.

        Args:
            workspace_id (str): ID of the clockify workspace.
            params (ReportGetParams, optional): Path parameters. Defaults to ReportGetParams().

        Returns:
            bytes | str | SummaryReport: Binary file if exportType is one of 'XLSX', 'PDF', otherwise SummaryReport or CSV as str
        """
        url = self.__url(workspace_id)
        return params.export_type in ['XLSX', 'PDF'] and self._get_file(url, params) or self.__post(url, params)

    def __url(self, workspace_id: str, report: str = 'summary') -> str:
        url = f"{REPORTS_URL}/workspaces/{workspace_id}/reports/{report}"
        return url
