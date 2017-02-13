# DisqusCommentParser 
This is an xml parsing tool used to grab disqus comments and sort them by thread into a CSV file. This tool works by doing two major steps: <ol><li>The tool grabs the thread ID's for each thread (called a post for this specific WordPress site I was using it for), and putting them into a dictionary</li>
<li>Reading each individual comment and appending them onto the list object that is tied to each keys value.</li> </ol>

Note: by sorting alphanumerically in Excel / Other CSV viewing tools you will get a file that shows the thread with its' URL followed by each individual comment in the following format: <ul> <li><b>Thread</b> </li> <li> Comment </li> <li>Any child comments (replies) </li> <li> Comment </li><li><b> Thread</b></li><li>etc</li> </ul>

This Format makes it quite useful for viewing comments that reply to one another. Below is an example for a single thread (which is not identical to how the file outputs currently). In the following example there is a thread item, followed by a comment which has one child comment, followed by a comment that has two child comments.

Example:
<table style="width:25%" align="left">
  <tr>
    <th align="left" width="150">Thread ID</th>
    <th align="left" width="200">Thread URL</th> 
    <th align="left" width="150">Post ID</th>
  </tr>
  <tr>
    <td>00000001</td>
    <td>generic.url/00000001</td>
    <td>N/A</td>
  </tr>
  <tr>
    <td>00000001</td>
    <td>generic.url/00000001/1</td>
    <td>1</td>
  </tr>
  <tr>
    <td>00000001</td>
    <td>generic.url/00000001/1/1</td>
    <td>1.1</td>
  </tr>
  <tr>
    <td>00000001</td>
    <td>generic.url/00000001/2</td>
    <td>2</td>
  </tr>
  <tr>
    <td>00000001</td>
    <td>generic.url/00000001/2/1</td>
    <td>2.1</td>
  </tr>
  <tr>
    <td>00000001</td>
    <td>generic.url/00000001/2/2</td>
    <td>2.2</td>
  </tr>
</table>
