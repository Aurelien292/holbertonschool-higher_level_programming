import os 

def generate_invitations(template,attendees):
    
    if not isinstance(template, str) or template is None:
        print("Template doit etre une chaine de caracteres.")
        return
    
    if not isinstance(attendees, list) or attendees is None:
        print("Attendees doit etre une liste.")
        return
    
    if not template:
        print("Template est vide, aucun fichier n'est genere")
        return
    if not attendees:
        print("attendees est vide,aucun fichier n'est genere")
        return
        
    for i, attendee in enumerate(attendees,start=1):
        name = attendee.get("name", "N/A")
        event_title = attendee.get("event_title", "N/A")
        event_date = attendee.get("event_date", "N/A")
        event_location = attendee.get("event_location", "N/A")

        # Remplacer les placeholders dans le modèle
        invitation = template.replace("{name}", name) \
                              .replace("{event_title}", event_title) \
                              .replace("{event_date}", event_date) \
                              .replace("{event_location}", event_location)
        output_filename = f"output_{i}.txt"
        
        if os.path.exists(output_filename):
            print("f{output_filename}déjà creer.")
            continue
        try:
            with open(output_filename, 'w') as file:
                file.write(invitation)
            print(f"Fichier {output_filename} généré avec succès.")
            
        except Exception as e:
            print(f"Erreur lors de la création du fichier {output_filename}: {e}")
            return