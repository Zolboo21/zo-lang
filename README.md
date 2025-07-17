# 🐚 Zo Language (Universal Programming Language)

**Zo** is an experimental **universal, English-like programming language** designed to be simpler than Python and as readable as SQL.

It compiles Zo code into executable Python (and in the future, other languages like Java).

---

## 🚀 Features

- ✅ English-like syntax  
- ✅ Simple, declarative statements  
- ✅ Compiles to Python (Java, JS coming soon)  
- ✅ Runs with one command: `./hello.zo`

---

## 🛠 Example

### **hello.zo**

```zo
print Hello,
print Welcome
```

### Run it:

```bash
./hello.zo
```

### Output:

```
Compiled to ./hello.py
Hello,
Welcome
```

---

## 🗂 Project Structure

```
zo-lang/
├── hello.zo            # Sample Zo file
├── hello.py            # Auto-generated Python output
├── zo.py               # CLI compiler/runner
├── src/
│   ├── zo_parser.py    # Parses Zo syntax into AST
│   └── zo_compiler.py  # Converts AST into Python code
```

---

## ⚙️ Setup & Usage

### Clone the repo

```bash
git clone https://github.com/Zolboo21/zo-lang.git
cd zo-lang
```

### Create a symbolic link for CLI usage

```bash
sudo ln -s $(pwd)/zo.py /usr/local/bin/zo
```

### Create the Zo runner script

```bash
sudo nano /usr/local/bin/zo-runner
```

Paste:

```bash
#!/bin/bash
zo "$@" --run
```

Then:

```bash
sudo chmod +x /usr/local/bin/zo-runner
```

### Write and run `.zo` files

Make sure the `.zo` file starts with this shebang:

```zo
#!/usr/bin/env zo-runner
print Hello,
print Welcome
```

Make it executable:

```bash
chmod +x hello.zo
./hello.zo
```

---

## 🛤 Roadmap

- [x] Python backend
- [ ] Add conditionals (`if`, `else`)
- [ ] Add loops (`for`, `while`)
- [ ] Java and JS backends
- [ ] Standard library
- [ ] Web REPL for Zo

---

## 👤 Author

**Zolboo Odonkhuu**  
🇲🇳 Based in Mongolia  
GitHub: [@Zolboo21](https://github.com/Zolboo21)

---

## 📄 License

MIT
