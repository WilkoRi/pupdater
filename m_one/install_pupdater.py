import os

def update_settings(settings_path):
    with open(settings_path, "r") as f:
        content = f.read()

    if "'pupdater'" not in content:
        print("➕ Toevoegen aan INSTALLED_APPS...")
        content = content.replace(
            "INSTALLED_APPS = [",
            "INSTALLED_APPS = [\n    'pupdater',"
        )

        with open(settings_path, "w") as f:
            f.write(content)
        print("✅ INSTALLED_APPS bijgewerkt.")

def update_urls(urls_path):
    with open(urls_path, "r") as f:
        lines = f.readlines()

    if not any("include('pupdater.urls')" in line for line in lines):
        print("➕ Toevoegen aan urls.py...")

        for i, line in enumerate(lines):
            if "from django.urls" in line and "include" not in line:
                lines[i] = line.strip() + ", include\n"
            if 'urlpatterns' in line:
                lines.insert(i + 1, "    path('pupdater/', include('pupdater.urls')),\n")
                break

        with open(urls_path, "w") as f:
            f.writelines(lines)
        print("✅ urls.py bijgewerkt.")

if __name__ == "__main__":
    project_dir = os.getcwd()
    settings_path = os.path.join(project_dir, "m_one", "settings.py")
    urls_path = os.path.join(project_dir, "m_one", "urls.py")

    update_settings(settings_path)
    update_urls(urls_path)
