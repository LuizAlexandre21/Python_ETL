from win32com.client import Dispatch
import pythoncom

class QlikView:
    def __init__(self):
    self.app = Dispatch('QlikTech.QlikView')

    def OpenDoc(self, docname):
        doc = self.app.OpenDoc(docname)
        return doc

    def CloseDoc(self, doc):
        doc.CloseDoc()

    def ManageDocument():
        docname = "c:\EXAMPLE.qvw"
        q = QlikView()
        version = q.app.QvVersion()
        print(version)
        doc = q.OpenDoc(docname)
        chart = doc.GetSheetObject("exampletable")
        chart.ExportBiff("c:\exampletable.xls")

        q.CloseDoc(doc)
        q.app.Quit()


if __name__ == '__main__':
    ManageDocument()

