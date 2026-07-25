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

<h1>Algorithm combinations</h1>
<p>created by Lábszki Zoltán</p>

TABLE_PLACEHOLDER

</body>
</html>

"""

tableTemplate = """
<table>
  <tr>
    <th>unique_id</th>
    <th>Combining Algorithms: </th>
    <th>ALGORITHM_COMBINATION_PLACEHOLDER</th>
  </tr>
TABLE_ROW_PLACEHOLDER
</table>

TABLE_PLACEHOLDER
"""

tableRowTemplate = """
  <tr>
    <td>UNIQUE_ID_PLACEHOLDER</td>
    <td><img src="IMAGE_PATH_PLACEHOLDER"></td>
    <td><p>ALGORITHM_STRING_PLACEHOLDER</p></td>
  </tr>
TABLE_ROW_PLACEHOLDER
"""




def CreateTableRow(imagePath, algorithmString):
    result = tableRowTemplate.replace("IMAGE_PATH_PLACEHOLDER", imagePath)
    result = result.replace("ALGORITHM_STRING_PLACEHOLDER", algorithmString)
    return result


def AddTableRowToTableTemplate(baseString, rowString):
    result = baseString.replace("TABLE_ROW_PLACEHOLDER", rowString)
    return result


def AddTableToHTML(baseString, tableString):
    result = baseString.replace("TABLE_PLACEHOLDER", tableString)




