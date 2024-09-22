# dotbak

Backup your dotfiles and configuration files in other directories such as `/etc`.

## 环境要求

- UNIX-like system (Linux, macOS, etc.)
- Python 3.5+

## Install

将 `dotbak.py` 文件放入你想存放备份文件的目录中。

```bash
mkdir your_backup_dir && cd your_backup_dir

# git
git clone https://github.com/yanyingwang/dotbak.git
# curl
curl -O https://raw.githubusercontent.com/yaragos/dotbak/main/dotbak.py
# wget
wget https://raw.githubusercontent.com/yaragos/dotbak/main/dotbak.py
```

创建 `dotbak.json` 并添加你要备份的文件或目录（参考 `dotbak.example.json`)。

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

非常简单的 python 脚本， 不需要任何第三方库。直接运行 `dotbak.py` 即可开始备份。

```bash
python3 dotbak.py
```

## 结语

仅仅是我平时用于备份的脚本，功能单一，无法在新系统中还原你的配置文件。如果你需要更高级的功能来管理你的 dotfiles，可以参考 [Dotbot](https://github.com/anishathalye/dotbot), [yadm](https://github.com/TheLocehiliosan/yadm) 等工具。

