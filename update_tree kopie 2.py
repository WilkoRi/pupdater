import subprocess

def update_tree():
    # Definieer het pad naar de map en het outputbestand
    project_path = "/Users/wilko/projecten/m_one_project"
    output_file = f"{project_path}/tree.txt"

    try:
        # Voer de 'tree' opdracht uit en schrijf de output naar tree.txt
        with open(output_file, "w") as file:
            subprocess.run(["tree", "-L", "3", project_path], stdout=file, check=True)
        print(f"De projectstructuur is bijgewerkt en opgeslagen in: {output_file}")
    except FileNotFoundError:
        print("De 'tree'-tool is niet geïnstalleerd. Installeer deze met 'brew install tree' op macOS.")
    except subprocess.CalledProcessError as e:
        print(f"Er is een fout opgetreden bij het genereren van de projectstructuur: {e}")

if __name__ == "__main__":
    update_tree()
