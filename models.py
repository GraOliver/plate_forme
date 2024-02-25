from django.db import models
"""
    Nous allons créer ici la base des données
"""
class Religion(models.Model):
    nom =models.CharField(max_length=25)
    
    def __str__(self):
        return self.nom
    
    class Meta :
        verbose_name="Religion"
        verbose_name_plural="Religions"
        
        
class Communaute(models.Model):
    nom = models.CharField(max_length=60)
    id_religion=models.ForeignKey(Religion,on_delete=models.DO_NOTHING)
    #annee_creation =models.DateField()
    visionaire =models.CharField(max_length=166)
    pasteurs=models.CharField(max_length=166)

    def __str__(self):
        return self.nom
    
    class Meta :
        verbose_name="Communauté"
        verbose_name_plural="Communautés"