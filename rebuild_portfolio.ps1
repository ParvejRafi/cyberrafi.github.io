# PowerShell script to rebuild modern portfolio
Write-Host 'Starting to rebuild modern portfolio HTML...'

# This will be a multi-part build
# Part 1: Read existing hero and about sections
$existingContent = Get-Content 'index.html' -Raw

# Find the About section end
$aboutEnd = $existingContent.IndexOf('</section>', $existingContent.IndexOf('id="about"'))
if ($aboutEnd -gt 0) {
    $headerAndAbout = $existingContent.Substring(0, $aboutEnd + 11)
    Write-Host 'Extracted header and about section'
    $headerAndAbout | Out-File 'temp_part1.html' -Encoding UTF8
} else {
    Write-Host 'Could not find About section'
}
