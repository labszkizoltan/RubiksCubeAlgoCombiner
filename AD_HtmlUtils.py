
htmlTemplate = """

<!DOCTYPE html>
<html>
<head>
<style>
table, th, td {
  border: 1px solid black;
}
</style>


<title>Page Title</title>
</head>
<body>

<h1>Sune algorithm combinations</h1>
<p>created by Lábszki Zoltán</p>

<table>
  <tr>
    <th>Image</th>
    <th>Algorithm</th>
  </tr>

TABLE_ROW_PLACEHOLDER
  
</table>


</body>
</html>

"""

tableRowTemplate = """
  <tr>
    <td><img src="IMAGE_PATH_PLACEHOLDER"></td>
    <td><p>ALGORITHM_STRING_PLACEHOLDER</p></td>
  </tr>
TABLE_ROW_PLACEHOLDER
"""


def CreateTableRow(imagePath, algorithmString):
    result = tableRowTemplate.replace("IMAGE_PATH_PLACEHOLDER", imagePath)
    result = result.replace("ALGORITHM_STRING_PLACEHOLDER", algorithmString)
    return result

def AddTableRowToTemplate(baseString, rowString):
    result = baseString.replace("TABLE_ROW_PLACEHOLDER", rowString)
    return result



