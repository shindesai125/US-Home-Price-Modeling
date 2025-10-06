param(
    [switch]$CreateGitHub,
    [string]$RepoName = ""
)

function Ensure-Git {
    if (!(Get-Command git -ErrorAction SilentlyContinue)) {
        $gitPath = 'C:\Program Files\Git\cmd\git.exe'
        if (Test-Path $gitPath) {
            $env:PATH += ";$(Split-Path $gitPath)"
            Write-Output "Temporarily added Git to PATH for this session."
        } else {
            Write-Error "Git not found. Please install Git from https://git-scm.com/download/win and re-run this script."
            exit 1
        }
    }
}

function Ensure-GitConfig {
    $name = git config --global user.name
    $email = git config --global user.email
    if (-not $name) {
        $name = Read-Host "Enter your name for git user.name"
        git config --global user.name "$name"
    }
    if (-not $email) {
        $email = Read-Host "Enter your email for git user.email"
        git config --global user.email "$email"
    }
}

function Init-And-Commit {
    $cwd = Get-Location
    if (!(Test-Path (Join-Path $cwd '.git'))) {
        git init
    } else {
        Write-Output "Repository already initialized."
    }

    git add .
    if (git diff --cached --quiet) {
        Write-Output "No changes to commit."
    } else {
        git commit -m "Initial commit — add project files and .gitignore"
        Write-Output "Committed initial project files."
    }
}

function Rename-To-Main {
    # Rename current branch to main
    git branch -M main
}

function Create-GitHub-And-Push {
    param($repoName)
    if (!(Get-Command gh -ErrorAction SilentlyContinue)) {
        Write-Error "GitHub CLI 'gh' not found. Install from https://cli.github.com/ or create the repo manually."
        return
    }
    if (-not $repoName) {
        $repoName = Read-Host "Enter GitHub repo name (will create under your account)"
    }
    gh repo create $repoName --public --source=. --remote=origin --push
}

Write-Output "Running repository setup..."
Ensure-Git
Ensure-GitConfig
Init-And-Commit
Rename-To-Main

if ($CreateGitHub) {
    Create-GitHub-And-Push -repoName $RepoName
}

Write-Output "Done. You can now use 'git status' or open the folder in your editor."
