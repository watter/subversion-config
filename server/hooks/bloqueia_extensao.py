#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys, pysvn, optparse
# vim:set ts=4 sw=4 sts=4 expandtab:
 	 	
#mensagem de erro apresentada ao usuario caso ele tente fazer um commit com arquivos nao permitidos

#error_msg = """\n\nNao foi possivel realizar o commit. \n\n\tAlguns arquivos nao sao versionados no SVN, eles devem ser colocados em outros locais:\n\t\t + jar,war,ear -> Archiva (maven.celepar.parana)\n\t\t + od(t|f), doc,xls,ppt,pdf -> Documentador (www.documentador.pr.gov.br)\n\t\t + tmp,swp,bak,out,exe,rar,zip -> nao sao permitidos \n\n\tOs seguintes arquivos do commit foram IMPEDIDOS de entrar no controle de versao:"""

error_msg = u"""\n\nNão foi possível realizar o commit. \n\n\tAlguns arquivos não são versionados no SVN, eles devem ser colocados em outros locais:\n\n\t\t + jar,war,ear -> Archiva (maven.celepar.parana)\n\n\t\t + od(t|f), doc,xls,ppt,pdf -> Documentador (www.documentador.pr.gov.br)\n\n\t\t + tmp,swp,bak,out,exe,rar,zip -> não são permitidos \n\n\tOs seguintes arquivos do commit foram impedidos de entrar no controle de versão:"""


#lista contendo as extensoes nao permitidas
extensoes_proibidas = ["zip","pdf","exe","jar","war","ear","swp","out","bak","tmp","doc","odf","odt","rar","xls","ppt"]

def main():
    repos = sys.argv[1]
    txn = sys.argv[2]
    files = get_files(repos, txn)
    files_extensoes_proibidas = check_extensoes(files)
    output = 0
    if len((files_extensoes_proibidas)) > 0:
        output = get_error_message(files_extensoes_proibidas)
        print >> sys.stderr, output.encode('utf-8')
    return output

#retorna um dicionario(hash) contendo o nome do arquivo e seu tamanho
def get_files(repos_path, txn):
    transaction = pysvn.Transaction(repos_path, txn)
    changed = transaction.changed()
    files = {}
    for file,attrs in transaction.changed().iteritems():
        if attrs[1] == pysvn.node_kind.file and not attrs[0] == 'D':
            files[file] = len(transaction.cat(file))
    return files

def check_extensoes(changed_files):
    files_extensoes_proibidas = {}
    for file in changed_files:
        extensao_arquivo = file.split(".")[-1]
	for extensao_proibida in extensoes_proibidas:
		if extensao_arquivo == extensao_proibida:
			files_extensoes_proibidas[file] = changed_files[file]

    return files_extensoes_proibidas

#retorna a mensagem de erro concatenada com a lista de arquivos nao permitidos
def get_error_message(files_extensoes_proibidas):
    output = "\n\n\t" + error_msg + "\n\t\t"
    for file in files_extensoes_proibidas:
        output = output + file + "\n\t\t"
    return output


if __name__ == "__main__":
    sys.exit(main())
