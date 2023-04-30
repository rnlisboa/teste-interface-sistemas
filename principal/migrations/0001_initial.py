# Generated by Django 4.2 on 2023-04-29 21:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ClasseToxicologica',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nivel_categoria', models.IntegerField()),
                ('descricao', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name_plural': 'Classes Toxicológicas',
            },
        ),
        migrations.CreateModel(
            name='Propriedade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=255)),
                ('cnpj', models.CharField(max_length=18)),
                ('local', models.TextField()),
                ('latitude', models.CharField(max_length=10)),
                ('longitude', models.CharField(max_length=10)),
            ],
            options={
                'verbose_name_plural': 'Propriedade',
            },
        ),
        migrations.CreateModel(
            name='ResponsaveisTecnicos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('cnpj', models.CharField(max_length=18)),
                ('numero_registro', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name_plural': 'Responsáveis técnicos',
            },
        ),
        migrations.CreateModel(
            name='ProdutorRural',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('propriedade', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='principal.propriedade')),
            ],
            options={
                'verbose_name_plural': 'Produtor rural',
            },
        ),
        migrations.CreateModel(
            name='DiagnosticoRecomendacaoTecnica',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cultura', models.CharField(max_length=255)),
                ('produto_comercial', models.CharField(max_length=255)),
                ('area_a_tratar', models.CharField(max_length=255)),
                ('volume_da_calda', models.CharField(max_length=255)),
                ('modalidade_aplicacao', models.CharField(max_length=255)),
                ('alvo', models.CharField(max_length=255)),
                ('intervalo_de_seguranca', models.CharField(max_length=255)),
                ('equipamento_aplicacao', models.CharField(max_length=255)),
                ('quantidade_a_adquirir', models.IntegerField()),
                ('numero_aplicacoes', models.IntegerField()),
                ('epoca_aplicacao', models.TextField()),
                ('classe_toxicologica', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='principal.classetoxicologica')),
            ],
            options={
                'verbose_name_plural': 'Diaginósticos e recomendações técnicas',
            },
        ),
    ]
