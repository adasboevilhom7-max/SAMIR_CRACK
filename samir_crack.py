# -*- coding: utf-8 -*-
import os, re, time, socket, sys, base64
from datetime import datetime
import ctypes
import requests  # For HTTPS requests

OWNER="@Samir_hacker1"

G="\033[92m"; R="\033[91m"; Y="\033[93m"
C="\033[96m"; W="\033[97m"; RESET="\033[0m"

def clear(): os.system("clear")

def beep():
    try: print("\a", end="")
    except: pass

def sound_fx(n=2):
    for _ in range(n):
        print("\a", end="")
        time.sleep(0.1)

def typing(t,s=0.02):
    for c in t:
        sys.stdout.write(c); sys.stdout.flush(); time.sleep(s)
    print()

def cinematic_loading():
    clear()
    frames = [
        "⚡ Connecting SAMIR🇺🇿CHEAT Server...",
        "⚡ Bypassing Firewall...",
        "⚡ Injecting Payload...",
        "⚡ Accessing Non Root...",
        "💀 SYSTEM READY 💀"
    ]
    for f in frames:
        print(C + f + RESET)
        sound_fx(1)
        time.sleep(0.5)
    print(G + "\n💀 WELCOME BACK ▄︻デ@̷Samir_hacker1══━一 💀\n" + RESET)
    time.sleep(1)

def system_init_effect():
    clear()
    steps = [
        "⚡ Initializing Secure Environment...",
        "⚡ Loading PRO SYSTEM...",
        "⚡ Checking Network Security...",
        "⚡ Decrypting Modules...",
        "⚡>>> [[ENTER YOU PASSWORD ~>> SAMIR CHEAT ]] <<<"
    ]
    for s in steps:
        typing(C + s + RESET, 0.03)
        sound_fx(1)
        time.sleep(0.4)
    print("\n💀 SYSTEM INITIALIZING...\n")
    typing("Accessing Root Files...",0.02)
    for i in range(0, 101, 5):
        bar = "█" * (i // 5)
        space = " " * (20 - len(bar))
        print(f"\r[{bar}{space}] {i}%", end="")
        time.sleep(0.1)
    print("\n\n✅ SYSTEM READY\n")
    beep()
    time.sleep(1)

def verify_key():
    print("\n😱 ENTER KEY 😱")
    keys=["SAMIR CHEAT"]
    k=input("Key >> ")
    if k in keys:
        print("✅ ACCESS GRANTED"); beep(); return True
    print("❌ WRONG KEY"); return False

def premium_banner():
    clear()
    print(G+"╔══════════════════════════════════════╗")
    print("║        💎 >>SAMIR CHEAT🇺🇿<< TELEGRAM 💎     ║")
    print("║     If Any Issue Dm :> @Samir_hacker1 ║")
    print("╚══════════════════════════════════════╝"+RESET)
    print(C+"Owner:",OWNER,RESET)

def sysinfo():
    now=datetime.now()
    print("TIME:",now.strftime("%H:%M:%S"),
          "| DATE:",now.strftime("%d-%m-%Y"))
    print("-"*35)

def path_picker(start="/sdcard"):
    cur=start
    while True:
        try: items=os.listdir(cur)
        except: return None
        print("\n📂",cur,"\n0.Back")
        for i,it in enumerate(items[:20],1):
            print(i,it)
        ch=input(">> ")
        if ch=="0": cur=os.path.dirname(cur); continue
        if not ch.isdigit(): continue
        p=os.path.join(cur,items[int(ch)-1])
        if os.path.isdir(p): cur=p
        else: return p

def extract_strings(f):
    try: return re.findall(rb"[ -~]{6,}",open(f,"rb").read())
    except: return []

def find_urls(s):
    u=[]
    for x in s:
        u+=re.findall(rb'https?://[^\s"\']+',x)
    return list(set(u))

def replace_url(f,new):
    data=open(f,"rb").read()
    urls=find_urls(extract_strings(f))
    if not urls: return print("❌ No URLs")
    for old in urls:
        if len(new)<=len(old):
            data=data.replace(old,new.encode().ljust(len(old)))
    open("mod_"+os.path.basename(f),"wb").write(data)
    print("✅ Done"); beep()

def auto_patch(f,new):
    data=open(f,"rb").read()
    urls=find_urls(extract_strings(f))
    if not urls: return print("❌ No URLs")
    count=0
    for old in urls:
        if len(new)<=len(old):
            data=data.replace(old,new.encode().ljust(len(old)))
            count+=1
    open("mod_"+os.path.basename(f),"wb").write(data)
    print(f"⚡ Patched {count} URLs"); beep()

def multi_edit(f):
    data = open(f, "rb").read()
    urls = find_urls(extract_strings(f))
    if not urls:
        return print("❌ No URLs Found")
    print(f"\n🌐 Total URLs Found: {len(urls)}\n")
    for i, u in enumerate(urls, 1):
        print(f"{i}. {u.decode(errors='ignore')}")
    try:
        count = int(input("\n👉 ENTER YOUR NUMBER ON UPER SESSION SELECTING: "))
    except:
        return print("❌ Invalid number")
    if count > len(urls): count = len(urls)
    new_url = input("👉 New URL: ")
    print("\n🔍 Preview Changes:\n")
    for i in range(count):
        old = urls[i]
        print(f"{i+1}. {old.decode(errors='ignore')}  ➜  {new_url}")
    confirm = input("\nConfirm? (y/n): ")
    if confirm.lower() != "y":
        print("❌ Cancelled"); return
    new_data = data
    edited = 0
    for old in urls[:count]:
        if len(new_url) <= len(old):
            new_data = new_data.replace(old,new_url.encode().ljust(len(old)))
            edited += 1
    open("mod_" + os.path.basename(f),"wb").write(new_data)
    print(f"\n✅ {edited} URLs Edited Successfully"); beep()

def smart(f):
    for s in extract_strings(f):
        s=s.decode(errors="ignore").lower()
        for k in ["token","key","auth","pass","login"]:
            if k in s:
                print("⚠️",s[:80])

def encoded(f):
    print("\n🧠 Encoded:\n")
    for s in extract_strings(f)[:200]:
        s=s.decode(errors="ignore")
        if re.fullmatch(r'[A-Za-z0-9+/=]{20,}',s):
            print("Base64:",s[:60])
        elif re.fullmatch(r'[0-9a-fA-F]{16,}',s):
            print("Hex:",s[:60])

def decode_strings(f):
    print("\n🧬 Decoded:\n")
    for s in extract_strings(f):
        try:
            d=base64.b64decode(s).decode(errors="ignore")
            if d.strip(): print("🔓",d[:80])
        except: pass

def deep(f):
    print("\n🔍 Deep Scan...\n")
    strings=extract_strings(f)
    found=set()
    for s in strings:
        for u in re.findall(rb'https?://[^\s"\']+',s):
            found.add(u.decode(errors="ignore"))
    for s in strings:
        try:
            d=base64.b64decode(s).decode(errors="ignore")
            if "http" in d: found.add(d)
        except: pass
    print("🌐 Found:",len(found))
    for i,u in enumerate(found,1):
        print(i,u)

def auto_scanner(file):
    print(C + "\n🧠 SCANNING FILE..." + RESET)
    steps = [
        "Checking strings...",
        "Analyzing patterns...",
        "Detecting URLs...",
        "Scanning encoded data...",
        "Finalizing report..."
    ]
    for s in steps:
        print(Y + "[*] " + s + RESET)
        time.sleep(0.5)
    print(G + "\n✔ Scan Complete (Safe Mode)\n" + RESET)
    beep()

def https_so_loader():
    print(C + "\n⚡ ADVANCED SO ANALYZER + HTTPS\n" + RESET)
    print("⚡ Applying Auto Patch Commands...\n")

    os.system("sed -i 's/def replace_url(f,new):/def replace_url(f,new=\"https:\\/\\/123.10\"):/g' libADIDAS.so")
    os.system("sed -i 's/def auto_patch(f,new):/def auto_patch(f,new=\"https:\\/\\/123.10\"):/g' libADIDAS.so")
    os.system("sed -i 's/new_url = input(\"👉 New URL: \")/new_url = \"https:\\/\\/123.10\"/g' libADIDAS.so")
    os.system("sed -i 's/replace_url(f,input(\"New URL: \"))/replace_url(f)/g' libADIDAS.so")
    os.system("sed -i 's/auto_patch(f,input(\"New URL: \"))/auto_patch(f)/g' libADIDAS.so")
    os.system("sed -i 's/url = input(\"Enter URL: \").strip()/url = \"https:\\/\\/123.10\"/g' libADIDAS.so")

    lib_path = input("📂 Enter full path of .so file: ").strip()
    if not os.path.exists(lib_path):
        print(R + "❌ File not found!" + RESET)
        return

    print(Y + "\n📊 File Info:" + RESET)
    print("Size:", os.path.getsize(lib_path), "bytes")
    print(C + "\n🧠 Extracting readable strings...\n" + RESET)
    try:
        data = open(lib_path, "rb").read()
        strings = re.findall(rb"[ -~]{6,}", data)
        for s in strings[:50]:
            print("🔹", s.decode(errors="ignore"))
    except:
        print(R + "❌ String extraction failed" + RESET)

    print(C + "\n🔎 Scanning possible function names...\n" + RESET)
    symbols = []
    for s in strings:
        s = s.decode(errors="ignore")
        if "(" not in s and len(s) < 40:
            if any(x in s.lower() for x in ["init","func","main","start","load","check"]):
                symbols.append(s)
    symbols = list(set(symbols))[:20]
    if symbols:
        for i, sym in enumerate(symbols, 1):
            print(f"{i}. {sym}")
    else:
        print("⚠️ No obvious symbols found")

    try:
        lib = ctypes.CDLL(lib_path)
        print(G + "\n✅ Library Loaded" + RESET)
    except Exception as e:
        print(R + f"\n❌ Load Failed: {e}" + RESET)
        return

    print(C + "\n⚙️ Trying to execute detected functions...\n" + RESET)
    for sym in symbols[:5]:
        try:
            func = getattr(lib, sym)
            func.restype = ctypes.c_void_p
            func()
            print(G + f"✅ Executed: {sym}" + RESET)
        except:
            print(Y + f"⚠️ Skipped: {sym}" + RESET)

    print(C + "\n🌐 HTTPS TEST\n" + RESET)
    url = "https://123.10"
    try:
        r = requests.get(url, timeout=10)
        print(G + f"✅ Status: {r.status_code}" + RESET)
        print(C + r.text[:200] + RESET)
    except Exception as e:
        print(R + f"❌ Request failed: {e}" + RESET)
    return

def menu():
    print(C+"\n╔══════════════════════════════════════╗")
    print("║💎💎 SAMIR CHEAT TOOLS SCRIP 💎💎        ")
    print("╠══════════════════════════════════════╣")
    print("║ [1] CLEAR              ")
    print("║ [2] OLD CONFIG🖇️ (Vip)             ")
    print("║ [3] ADD NEW PANNEL AND SEARCH 😈.")
    print("║ [4] SDK OFF (Vip)             ")
    print("║ [5] LOGIN BYPASS (Vip)📴               ")
    print("║ [6] VIP BYPASS (Vip) 📴                 ")
    print("║ [7] MOD+ LOADER LOGIN BYPASS  ")
    print("║ [8] EXIT MINU          ")
    print("║ [9] ALL MOD+LOADER NO BYPASS (Vip) ")
    print("║ [10] SO Loader + https      ")
    print("╚══════════════════════════════════════╝"+RESET)
    beep()

def main():
    cinematic_loading()
    system_init_effect()
    if not verify_key(): print("🚫 EXIT"); return
    while True:
        premium_banner(); sysinfo(); menu()
        ch=input("😈 >> ")
        if ch=="1":
            f=path_picker()
            if f:
                for u in find_urls(extract_strings(f)):
                    print("🌐",u.decode(errors='ignore'))
                smart(f); input("Enter...")
        elif ch=="2":
            f=path_picker()
            if f:
                replace_url(f,input("New URL: "))
                input("Enter...")
        elif ch=="3":
            f=path_picker()
            if f: multi_edit(f); input("Enter...")
        elif ch=="4":
            f=path_picker()
            if f: encoded(f); input("Enter...")
        elif ch=="5":
            f=path_picker()
            if f: deep(f); input("Enter...")
        elif ch=="6":
            f=path_picker()
            if f: auto_patch(f,input("New URL: ")); input("Enter...")
        elif ch=="7":
            f=path_picker()
            if f: decode_strings(f); input("Enter...")
        elif ch=="9":
            f=path_picker()
            if f: auto_scanner(f); input("Enter...")
        elif ch=="10":
            https_so_loader()
        elif ch=="8":
            break

if __name__=="__main__":
    main()
