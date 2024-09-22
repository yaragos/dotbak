# dotbak

**Read this in other languages: [English](README.md), [中文](README_zh.md).**

Backup your dotfiles and configuration files in other directories such as `/etc`.

## Requirements

- UNIX-like system (Linux, macOS, etc.)
- Python 3.5+

## Install

Place the `dotbak.py` file in the directory where you want to store the backup files.

```bash
mkdir your_backup_dir && cd your_backup_dir

# git
git clone https://github.com/yanyingwang/dotbak.git
# curl
curl -O https://raw.githubusercontent.com/yaragos/dotbak/main/dotbak.py
# wget
wget https://raw.githubusercontent.com/yaragos/dotbak/main/dotbak.py
```

Create `dotbak.json` and add the files or directories you want to back up (refer to `dotbak.example.json`).

```json
{
  "home": [
    ".vimrc",
    ".config/nvim",
    ".config/starship.toml"
  ],
  "etc": [
    "vim"
  ]
}
```

## Usage

A very simple Python script that does not require any third-party libraries. Just run dotbak.py to start the backup.

```bash
python3 dotbak.py
```

## Conclusion

This is merely a script I use for backup. It has a single function and cannot restore your configuration files on a new system. If you need more advanced features to manage your dotfiles, you can refer to tools like Dotbot, yadm, etc.
